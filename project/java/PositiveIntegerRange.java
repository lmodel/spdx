package example;

/* metamodel_version: 1.12.0 */
/* version: 3.0.1 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A tuple of two positive integers that define a range.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PositiveIntegerRange  {

  private URI type;
  private Integer beginIntegerRange;
  private Integer endIntegerRange;


}