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
  A mathematically calculated representation of a grouping of data.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Hash extends IntegrityMethod {

  private String algorithm;
  private String hashValue;


}