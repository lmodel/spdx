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
  Provides an independently reproducible mechanism that permits verification of a specific Element.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class IntegrityMethod  {

  private URI type;
  private String comment;


}